# dans header, récupérer canaux + taille d'un échantillon + taille des données
# dans data, data[0], data[O:2]
# byte = octet = 8 bits
# P = open('...','rb')  rb pour read byte
# pour convertir en entier = import struct et utiliser les méthodes pack et unpack
# unpack(data[0:2],format ie sur combien d'entiers) passe de binaire à entier
# buffer ensemble de données binaires
# si un échantillon de 8 bits avec 2 canaux, on a 16 bits au total

import struct
from struct import unpack_from

### exercice 1 — Lecture et extraction des échantillons

def extract_wav_data(fichier):
    with open(fichier, 'rb') as f:
        data = f.read()

    ### lecture du header
    
    # nombre de canaux (2 octets d'ou 'H' à position 22)
    canaux = unpack_from('H', data, 22)[0]

    # bits par échantillon (2 octets à position 34)
    bits_par_ech = unpack_from('H', data, 34)[0]
    octets_par_ech = bits_par_ech // 8  # 16 bits //8 → 2 octets : un échantillon a 2 octets par voie 

    # taille des données audio (4 octets donc 'I' à position 40)
    taille_data = unpack_from('I', data, 40)[0]

    # nombre total d'échantillons (par canal) : taille des données au TOTAL / nombre de canaux*nombre d'éch par canal
    nb_ech_par_voie = taille_data // (canaux * octets_par_ech)

    print(f'Canaux : {canaux}',f'Bits par échantillon : {bits_par_ech}',f'Nombre d échantillons par voie : {nb_ech_par_voie}')

    ### extraction des données audio

    offset = 44  # données audio commencent à la position 45-1=44
    liste = []

    # on lit les données 4 bytes par 4 bytes (2 canaux × 2 octets chacun)
    for i in range(nb_ech_par_voie):
        pos_init = offset + i * 4  # chaque bloc = 4 octets (2 par canal)
        gauche, droite = unpack_from('hh', data, pos_init) # pour canal de 'gauche' et de 'droite'
        liste.append((gauche, droite))  # tuple pour canal gauche et droit

    return liste, canaux, bits_par_ech


# exercice 2 — Reconstruction d'un fichier WAV

def save_wav(output_file, samples, canaux=2, bits_par_ech=16, frequence=44100):
    with open(output_file, 'wb') as f:

        # paramètres 
        octets_par_ech = bits_par_ech // 8
        nb_ech = len(samples)
        taille_data = nb_ech * canaux * octets_par_ech
        taille_fichier = 36 + taille_data
        byte_rate = frequence * canaux * octets_par_ech
        block_align = canaux * octets_par_ech

        f.write(b'RIFF')
        f.write(struct.pack('I', taille_fichier))  # Taille totale - 8 (8 pour place prise par riff et wave)
        f.write(b'WAVE')

        f.write(b'fmt ')
        f.write(struct.pack('I', 16))  # Taille du sous-bloc fmt
        f.write(struct.pack('H', 1))   # Format audio PCM
        f.write(struct.pack('H', canaux))
        f.write(struct.pack('I', frequence))
        f.write(struct.pack('I', byte_rate))
        f.write(struct.pack('H', block_align))
        f.write(struct.pack('H', bits_par_ech))

        # Chunk data
        f.write(b'data')
        f.write(struct.pack('I', taille_data))

        # écriture des échantillons
        for frame in samples:
            # On suppose frame = (gauche, droite)
            if canaux == 1:
                frame = [frame]
            for val in frame:
                if bits_par_ech == 16:
                    f.write(struct.pack('h', val))  # Échantillon 16 bits signé
                elif bits_par_ech == 8:
                    f.write(struct.pack('B', val))  # Échantillon 8 bits non signé
                else:
                    raise NotImplementedError('Format non supporté')

    print(f"Fichier '{output_file}' créé avec succès")


liste, canaux, bits = extract_wav_data('the_wall.wav')
save_wav('copie_the_wall.wav', liste, canaux=canaux, bits_par_ech=bits)

