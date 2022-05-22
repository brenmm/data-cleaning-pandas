def nulos_col_100(df):
    
    """
    Esta función muestra el porcentaje de valores NaN en cada
    columna del DataFrame
        
    """
    
    nulos = df.isna().sum()
    return nulos[nulos > 0] / len(df) * 100


def limpiar_columnas(df):
    """
    Esta función limpia de puntuación etc todas las columnas 
    del DataFrame
        
    """
    df.columns = df.columns.str.lower()
    df.columns = df.columns.str.replace(r"\."," ")
    df.columns = df.columns.str.replace(r"\s$","")
    df.columns
    return df.columns


def limpiar_fatal(df):
    """
    Esta función elimina duplicados y corrige errores 
    gramaticales o de puntuación en Fatal (Y/N)
    
    """
    df['Fatal (Y/N)'] = df['Fatal (Y/N)'].str.strip()
    df['Fatal (Y/N)'] = df['Fatal (Y/N)'].str.replace('n', 'N')
    df['Fatal (Y/N)'] = df['Fatal (Y/N)'].str.replace('F', 'Y')
    df['Fatal (Y/N)'] = df['Fatal (Y/N)'].str.replace('UNKNOWN', 'Unknown')
    df['Fatal (Y/N)'].fillna("Unknown",inplace=True) 
    df['Fatal (Y/N)'] = df['Fatal (Y/N)'].apply(lambda x: "N" if x == " N" else x)
    df['Fatal (Y/N)'] = df['Fatal (Y/N)'].apply(lambda x: "Y" if x == "y" else x)
    return df["Fatal (Y/N)"]


def limpiar_type(df):
    """
    Esta función elimina duplicados y corrige errores 
    gramaticales o de puntuación en Type
    
    """
    df['Type'].fillna("Unknown",inplace=True)
    df["Type"] = df["Type"].str.replace('Invalid', 'Unknown')
    df["Type"] = df["Type"].str.replace('Sea Disaster', 'Unprovoked')
    df["Type"] = df["Type"].str.replace('Questionable', 'Unknown')
    df.loc[df['Type'].str.startswith('Boat'), "Type"] = 'Provoked'
    return df.Type


def limpiar_sex(df): 
    """
    Esta función elimina duplicados y corrige errores 
    gramaticales o de puntuación en Sex
    
    """
    df.Sex = df.Sex.fillna("UNKNOWN")
    df.Sex = df.Sex.str.replace(r"(.*)?M(.*)?","M")
    df.Sex = df.Sex.str.replace(r"(.*)?N(.*)?","UNKNOWN")
    df.Sex = df.Sex.str.replace(".","UNKNOWN")
    df.Sex = df.Sex.str.replace("lli","UNKNOWN")
    return df.Sex

def limpiar_country(df):
    """
    Esta función elimina duplicados y corrige errores 
    gramaticales o de puntuación en Country
    
    """
    df.Country = df.Country.str.lower()
    df.Country = df.Country.fillna("unknown")
    df.Country = df.Country.str.replace("usa", "united states")
    df.Country = df.Country.str.replace("roatan", "honduras")
    df.Country = df.Country.str.replace("tobago", "trinidad y tobago")
    df.Country = df.Country.str.replace("bahamas", "the bahamas")
    df.Country = df.Country.str.replace("england", "united kingdom")
    df.Country = df.Country.str.replace("british isles", "united kingdom")
    df.Country = df.Country.str.replace("england", "united kingdom")
    df.Country = df.Country.str.replace("reunion", "réunion")
    df.Country = df.Country.str.replace("okinawa", "japan")
    df.Country = df.Country.str.replace("azores", "portugal")
    df.Country = df.Country.str.replace("columbia", "colombia")
    df.Country = df.Country.str.replace("new britain", "papua new guinea")
    df.Country = df.Country.str.replace("new guinea", "papua new guinea")
    df.Country = df.Country.str.replace("british new guinea", "papua new guinea")
    df.Country = df.Country.str.replace("admiralty islands", "papua new guinea")
    df.Country = df.Country.str.replace("ghana", "republic of ghana")
    df.Country = df.Country.str.replace("guinea", "republic og guinea")
    df.Country = df.Country.str.replace("british west indies", "west indies")
    df.Country = df.Country.str.replace("burma", "republic of the union of myanmar")
    df.Country = df.Country.str.replace("san domingo", "republica dominicana")
    df.Country = df.Country.str.replace("reunion islands", "réunion")
    df.Country = df.Country.str.replace("curacao", "curaçao")
    df.Country = df.Country.str.replace("maldives", "republic of maldives")
    df.Country = df.Country.str.replace("st helena, british overseas territory", "saint helena")
    df.Country = df.Country.str.replace("comoros", "union of comoros")
    df.Country = df.Country.str.replace("st martin", "saint martin")
    df.Country = df.Country.str.replace("kiribati", "republic of kiribati")
    df.Country = df.Country.str.replace("seychelles", "republic of seychelles")
    df.Country = df.Country.str.replace("south korea", "republic of korea")
    df.Country = df.Country.str.replace("nevis", "Saint Kitts and Nevis")
    df.Country = df.Country.str.replace("gulf of aden", "yemen")
    df.Country = df.Country.str.replace("st maartin", "saint martin")
    df.Country = df.Country.str.replace("grand cayman", "cayman islands")
    df.Country = df.Country.str.replace("palau", "republic of palau")
    df.Country = df.Country.str.replace("federated states of micronesia", "micronesia")
    df.Country = df.Country.str.replace("andaman", "andaman islands")
    df.Country = df.Country.str.replace("gabon", "the gabonese republic")    
    df.Country = df.Country.str.replace(r"(.*)?ocean(.*)?", "unknown")
    df.Country = df.Country.str.replace(r"(.*)?sea(.*)?", "unknown")
    return df.Country


def limpiar_area(df):
    """
    Esta función elimina duplicados y corrige errores 
    gramaticales o de puntuación en Area
    
    """
    df.Area = df.Country.fillna("unknown")
    df.Area = df.Area.str.replace("Victoria ", "Victoria")
    df.Area = df.Area.str.replace("Torres Strait", "Queensland")
    df.Area = df.Area.str.replace("Torres Strait ", "Queensland")
    df.Area = df.Area.str.replace("Queensland ", "Queensland")
    df.Area = df.Area.str.replace("Between Timor & Darwin, Australia", "Northern Territory")
    df.Area = df.Area.str.replace("Westerm Australia", "Western Australia")
    df.Area = df.Area.str.replace("Between Timor and Darwin, Australia", "Northern Territory")
    return df.Area


















    