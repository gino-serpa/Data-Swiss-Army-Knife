import pandas as pd

def scielo_wos_info():
    info_string ='''
    https://images.webofknowledge.com/images/help/WOK/hs_selo_fieldtags.html
    SciELO Citation Index Field Tags
    These two-character field tags identify fields in records that you e-mail, export, or save. They cover various publications.

    FN
    File Name

    VR
    Version Number

    PT
    Publication Type

    AU
    Authors

    BE
    Editors

    TI
    English Document Title (An English Document Title may have a field tag of X1, Y1, or Z1)

    S1
    Full Source Title (Korean or Other Languages)

    X1
    Spanish Document Title (A Spanish Document Title may have a field tag of T1, Y1, or Z1)

    Y1
    Portuguese Document Title (A Portuguese Document Title may have a field tag of T1, X1, or Z1)

    Z1
    Other Languages Document Title (A document title may have a field tag of T1, X1, or Y1)

    SO
    Source

    LA
    Language

    DT
    Document Type

    DE
    English Author Keywords

    X5
    Spanish Author Keywords

    Y5
    Portuguese Author Keywords

    Z5
    Author Keywords (Other Languages)

    AB
    English Abstract

    X4
    Spanish Abstract

    Y4
    Portuguese Abstract

    Z4
    Abstract (Other Languages)

    C1
    Addresses

    EM
    E-mail Address

    RI
    ResearcherID Number

    OI
    ORCID Identifier (Open Researcher and Contributor ID)

    CR
    Cited References

    NR
    Cited Reference Count

    TC
    SciELO Citation Index Times Cited Count

    Z9
    Total Times Cited Count (Web of Science Core Collection, BIOSIS Citation Index, Chinese Science Citation Database, Data Citation Index, Russian Science Citation Index, SciELO Citation Index)

    U1
    Usage Count (Last 180 Days)

    U2
    Usage Count (Since 2013)

    PU
    Publisher

    PI
    Publisher City

    PA
    Publisher Address

    SN
    International Standard Serial Number (ISSN)

    PD
    Publication Date

    PY
    Year Published

    VL
    Volume

    IS
    Issue

    BP
    Beginning Page

    EP
    Ending Page

    DI
    Digital Object Identifier (DOI)

    EC
    SciELO Categories

    C2
    SciELO Collection

    SC
    Research Areas

    UT
    Accession Number

    OA
    Open Access Indicator

    HP
    ESI Hot Paper. Note that this field is valued only for ESI subscribers

    HC
    ESI Highly Cited Paper. Note that this field is valued only for ESI subscribers

    DA
    Date this report was generated

    ER
    End of Record

    EF
    End of File


    '''
    print(info_string)
    return

def ingest_wos_scielo_file(file_name):
    # (tdl) Before wqhat follows we should have chardet to avoid format problems
    # import chardet
    # rawdata = open ('data/savedrecs.txt',"rb").read()
    # chardet.detect(rawdata) <- Inspect this dict

    df = pd.read_csv(file_name,index_col=False, sep='\t')
    columns={'PT':'publication type',
         'AU': 'authors',
         'BE': 'editors',
         'TI': 'title',
         'X1': 'spanish title',
         'Y1': 'portuguese title',
         'Z1': 'other language title',
         'SO': 'source',
         'LA': 'language',
         'DT': 'document type',
         'DE': 'english author keywords',
         'X5': 'spanish author Keywords',
         'Y5': 'portuguese author keywords',
         'Z5': 'other language author keywords',
         'AB': 'abstract',
         'X4': 'spanish abstract',
         'Y4': 'portuguese abstract',
         'Z4': 'other language abstract',
         'C1': 'addresses',
         'EM': 'emails ',
         'RI': 'research id number',
         'OI': 'orchid id',
         'CR': 'cited references',
         'NR': 'cited references count',
         'TC': 'scielo citation index times cited count',
         'Z9': 'total times cited count',
         'U1': 'usage count 180',
         'U2': 'usage count 2013',
         'PU': 'publisher',
         'PI': 'publisher city',
         'PA': 'publisher address',
         'SN': 'issn',
         'PD': 'pub date',
         'PY': 'pub year',
         'VL': 'volume',
         'IS': 'issue',
         'BP': 'beggining page',
         'EP': 'ending page',
         'DI': 'doi',
         'EC': 'scielo categories',
         'C2': 'scielo collection',
         'SC': 'research areas',
         'UT': 'accession number',
         'OA': 'open access indicator',
         'HC': 'highly cited',
         'HP': 'hot paper',
         'DA': 'report date'}
    df=df.rename(columns, axis=1)
    return df

def get_english_author_keywords(keyword_string):
    if keyword_string!=keyword_string:
        return []
    english_author_keywords = keyword_string.split('; ')
    return english_author_keywords

def get_addresses(addresses_string):
    # Break the string by the [ to break into groups
    # The first element is blank
    alpha=addresses_string.split('[')[1:]

    addresses = {}
    # Now for each element brak by the closing bracket
    groups = [item.split(']') for item in alpha]

    return addresses

def get_scielo_dicts(df):
    authors = {}
    papers  = {}
    for idx,row in df.iterrows():
        id            = row['accession number']
        title         = row['title']
        spanish_title = row['spanish title']
        portuguese_title = row['portuguese title']
        other_language_title = row['other language title']
        source = row['source']
        language = row['language']
        english_author_keywords = \
                get_english_author_keywords(row['english author keywords'])
        authors_list = row['authors'].split('; ')
        year = int(row['pub year'])
        addresses = get_addresses(row['addresses'])
        papers[id] = {
               'title':title,
               'authors': authors_list,
               'year': year,
               'spanish title': spanish_title,
               'portuguese title': portuguese_title,
               'othe language title': other_language_title,
               'source': source,
               'language': language,
               'english author keywords':english_author_keywords
                    }

        # Take care of the authors dict
        for author in authors_list:
            if author not in authors:
                authors[author] = {'papers_list':[id]}
            else:
                authors[author]['papers_list'].append(id)

    return authors, papers
