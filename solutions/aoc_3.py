import pandas as pd


def create_df(l):
    df = pd.DataFrame()
    df['str'] = l
    df = df['str'].str.split('', expand=True)
    df = df.drop(0, axis= 1)
    df = df.drop(13, axis= 1)
    df = df.astype('int32')
    return df


def calc_power_rate(l):

    df = create_df(l)
    counts = []
    for i in range(1, 13):
        counts += [sum(df[i])]
    half = len(df) / 2
    gamma = map(lambda c: '1' if c > half else '0', counts)
    epsi = map(lambda c: '0' if c > half else '1', counts)

    gamma = int(''.join(gamma), 2)
    epsi = int(''.join(epsi), 2)
    return gamma * epsi


def search(l):
    df = create_df(l)

    def search_aux(df, idx, criteria_most):
        if len(df) == 1:
            return df

        count = sum(df[idx])
        length = len(df)
        if criteria_most:
            bit_to_keep = 1 if (count >= (length / 2)) else 0
        else:
            bit_to_keep = 1 if (count < (length / 2)) else 0

        df2 = df[df[idx] == bit_to_keep]
        return search_aux(df2, idx + 1, criteria_most)

    ogr = search_aux(df, 1, True)
    csr = search_aux(df, 1, False)
    ogr = int(''.join(ogr.astype('str').values.flatten().tolist()), 2)
    csr = int(''.join(csr.astype('str').values.flatten().tolist()), 2)

    return ogr * csr
