import pandas as pd
import chardet
import pathlib

countries ={'Angola':       ['Angola'],
            'Argentina':    ['Argentina'],
            'Australia':    ['Australia'],
            'Austria':      ['Austria'],
            'Barbados':     ['Barbados', 'BARBADOS'],
            'Belgium':      ['Belgium','Bélgica'],
            'Bolivia':      ['Bolivia'],
            'Brazil':       ['Brazil','Brasil','BRAZIL'],
            'Bulgaria':     ['Bulgaria'],
            'Canada':       ['Canada','CANADA','Canadá'],
            'China':        ['China','PEOPLES R CHINA','PEOPLES R CHINA',
                                "People's Republic of China"],
            'Colombia':     ['Colombia'],
            'Croatia':      ['Croatia'],
            'Cuba':         ['Cuba'],
            'Chile':        ['Chile'],
            'Colombia':     ['Colombia'],
            'Costa Rica':   ['Costa Rica'],
            'Denmark':      ['Denmark'],
            'Dominican Republic': ['Dominican Republic', 'República Dominicana'],
            'Ecuador':      ['Ecuador'],
            'El Salvador':  ['El Salvador'],
            'Finland':      ['Finland'],
            'France':       ['France','Francia'],
            'Germany':      ['Germany','Alemania','Deutschland'],
            'Greece':       ['Greece'],
            'Guatemala':    ['Guatemala'],
            'Guyana':       ['Guyana', 'GUYANA'],
            'Hong Kong':    ['Hong Kong'],
            'Honduras':     ['Honduras'],
            'Indonesia':    ['Indonesia'],
            'India':        ['India'],
            'Iran':         ['Iran'],
            'Iraq':         ['Iraq'],
            'Italy':        ['Italy','ITALY','Itália','Italia'],
            'Jamaica':      ['Jamaica'],
            'Japan':        ['Japan', 'JAPAN','Japón'],
            'Lithuania':    ['Lithuania'],
            'Macedonia':    ['Macedonia'],
            'Mali':         ['Mali'],
            'Mexico':       ['Mexico', 'México'],
            'Mozambique':   ['Mozambique'],
            'Netherlands':  ['Netherlands', 'Holanda'],
            'New Zealand':  ['New Zealand', 'Nueva Zelanda'],
            'Nicaragua':    ['Nicaragua'],
            'Nigeria':      ['Nigeria'],
            'Norway':       ['Norway', 'Noruega'],
            'Paraguay':     ['Paraguay','Paraguai'],
            'Peru':         ['Peru', 'Perú'],
            'Poland':       ['Poland'],
            'Portugal':     ['Portugal'],
            'Puerto Rico':  ['Puerto Rico'],
            'Russia':       ['Russia', 'Rusia'],
            'Saudi Arabia': ['Saudi Arabia'],
            'Serbia':       ['Serbia'],
            'Slovenia':     ['Slovenia'],
            'South Africa': ['South Africa'],
            'Sri Lanka':    ['Sri Lanka'],
            'Spain':        ['Spain','España','Espanha'],
            'Sweden':       ['Sweden'],
            'Switzerland':  ['Switzerland'],
            'Turkey':       ['Turkey'],
            'Ukraine':      ['Ukraine'],
            'United Arab Emirates': ['United Arab Emirates','U Arab Emirates'],
            'United Kingdom': ['United Kingdom', 'UK', 'ENGLAND','Inglaterra'],
            'Uruguay':      ['Uruguay'],
            'USA':          ['USA', 'Estados Unidos', 'United States','EE.UU',
                             'United States of América','EE. UU',
                             'United States of America',
                             'Estados Unidos de América'],
            'Venezuela':    ['Venezuela','República Bolivariana de Venezuela'],
            'Vietnam':      ['Vietnam'] }

def verify_country(country):
    country=country.strip('.')
    for canonical_name in countries:
        for alias in countries[canonical_name]:
            if alias.lower()==country.lower():
                return canonical_name
    print(country, ' not in datbase' )
    return 'No country available'

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

def ingest_wos_scielo_folder( data_folder = pathlib.Path.cwd()/'data' ):
    '''
    Ingests the scielo files in data_folder and returns a single dataframe
    with all the records

    Input:
        data_folder: Folder containing all the data files.
                     Defaults to 'data' in the current working directory
    Returns:
        df: Pandas dataframe with all the records
    '''

    # Check if folder exist and if there is data in the folder
    if not data_folder.exists():
        print(f'Data folder {str(data_folder)} does not exist!')
        return



    encoding = 'unknown'

    df_list = []
    for data_file in data_folder.glob('*.txt'):
        if encoding == 'unknown':
            rawdata = open (data_file,"rb").read()
            encoding = chardet.detect(rawdata)['encoding']
            print('Encoding: ', encoding)
        df_list.append(ingest_wos_scielo_file(data_file, encoding))
    df = pd.concat(df_list)

    return df

def ingest_wos_scielo_file(file_name, encoding):

    df = pd.read_csv(file_name,
                     encoding=encoding,
                     index_col=False,
                     sep='\t')
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

def get_addresses(alpha):
    if alpha!=alpha:
        return {}
    # Define an empty dict that will have the info we need
    addresses = {}

    # Break by the leading '[' of each author group
    alpha = alpha.split('[')[1:]

    # Each group now is divided in authors and an institution
    groups = [ item.split(']') for item in alpha]

    # Clean up each group and assign info to dict
    for pair in groups:
        if len(pair)!=2:
            print('FAULTY FORMAT: ', pair)
            return addresses
        (people, place) = pair
        place = place.strip('; ')
        people = people.split('; ')
        people = [item.replace('.', ' ').strip(' ').replace('  ',' ') \
                         for item in people]
        for author in people:
            addresses[author]=place
    return addresses

def get_author_list(author_str):
    author_list = author_str.split('; ')
    author_list = [item.replace('.',' ').strip(' ').replace('  ',' ') \
                    for item in author_list]
    return author_list

def get_scielo_dicts(df):
    authors = {}
    papers  = {}
    institutions = {}
    counter = 0
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
        authors_list = get_author_list(row['authors'])
        year = int(row['pub year'])
        addresses = get_addresses(row['addresses'])
        institution_list = list(set(list(addresses.values())))

        # Take care of papers dict
        papers[id] = {
               'title':title,
               'authors': authors_list,
               'year': year,
               'spanish title': spanish_title,
               'portuguese title': portuguese_title,
               'othe language title': other_language_title,
               'source': source,
               'language': language,
               'english author keywords':english_author_keywords,
               'institutions':institution_list
                    }

        # Take care of the authors dict
        for author in authors_list:
            if author not in authors:
                authors[author] = {'papers_list':[id]}
                authors[author]['institutions']  = []
            else:
                authors[author]['papers_list'].append(id)
        for author in addresses:
            institution = addresses[author]
            if institution not in authors[author]['institutions']:
                authors[author]['institutions'].append(institution)

        # Take care of institutions
        for institution in institution_list:
            if institution not in institutions:
                country = institution.split(',')[-1].strip(' ')
                country = verify_country(country)
                institutions[institution]=\
                    {'papers':[id],
                    'country':country}
            else:
                institutions[institution]['papers'].append(id)
    print(counter)
    return authors, papers, institutions
