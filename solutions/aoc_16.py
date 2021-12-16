from math import prod


def decoder_1(l):
    packet = parse(l)
    return sum_versions(packet)

def sum_versions(x):
    if x['type'] != 4:
        kids = sum(map(sum_versions, x['value']))
    else:
        kids = 0
    return x['version'] + kids


def interpret(x):
    typ = x['type']
    if typ == 4:
        return x['value']
    else:
        kids = list(map(interpret, x['value']))
        if typ == 0:
            return sum(kids)
        elif typ == 1:
            return prod(kids)
        elif typ == 2:
            return min(kids)
        elif typ == 3:
            return max(kids)
        elif typ == 5:
            if kids[0] > kids[1]:
                return 1
            else:
                return 0
        elif typ == 6:
            if kids[0] < kids[1]:
                return 1
            else:
                return 0
        elif typ == 7:
            if kids[0] == kids[1]:
                return 1
            else:
                return 0





def parse(l):
    hex = l[0]
    binary = ''.join(hexMap[h] for h in hex)
    gen = (b for b in binary)
    return parse_packet(gen)


def parse_packet(gen):

    packetVersion = n_bits_as_int(3, gen)

    if packetVersion is None:
        return None

    packetTypeID = n_bits_as_int(3, gen)

    if packetTypeID == 4:
        # literal
        litBits = []
        while (n_bits_as_int(1,gen) == 1):
            litBits.extend(n_bits(4, gen))
        else:
            litBits.extend(n_bits(4, gen))

        litValue = bits_as_int(litBits)

        return { 'version': packetVersion,
                 'type': packetTypeID,
                 'value': litValue
                 }

    else:
        length_type_id = n_bits_as_int(1, gen)
        if length_type_id == 0:
            # total length of sub-bits
            total_packets_length = n_bits_as_int(15, gen)
            child_packet_stream = (b for b in n_bits(total_packets_length, gen))
            child_packets = []
            while True:
                cp = parse_packet(child_packet_stream)
                if cp is None:
                    break
                child_packets.append(cp)

            return {'version': packetVersion,
                    'type': packetTypeID,
                    'value': child_packets
                    }

        else:
            # sub-packet count
            sub_packet_count = n_bits_as_int(11, gen)
            child_packets = []
            for i in range(0, sub_packet_count):
                child_packets.append(parse_packet(gen))
            return {'version': packetVersion,
                    'type': packetTypeID,
                    'value': child_packets
                    }

def n_bits_as_int(n, gen):
    bits = []
    for x in range(0, n):
        nb = next(gen, None)
        if nb is None:
            return None
        bits.append(nb)

    return int(''.join(bits), 2)

def n_bits(n, gen):
    bits = []
    for x in range(0, n):
        bits.append(next(gen))
    return bits

def bits_as_int(bits):
    return int(''.join(bits), 2)



hexMap = {
    "0": "0000",
    "1": "0001",
    "2": "0010",
    "3": "0011",
    "4": "0100",
    "5": "0101",
    "6": "0110",
    "7": "0111",
    "8": "1000",
    "9": "1001",
    "A": "1010",
    "B": "1011",
    "C": "1100",
    "D": "1101",
    "E": "1110",
    "F": "1111"
}

def decoder_2(l):
    packet = parse(l)
    return interpret(packet)
