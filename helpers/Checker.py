
def CheckUrl(url):
    url=url["url"]
    data=[]
    steps="path has the next steps:"
    parameters="parameters are:"
    ProtocolCheck=url.split("://")[0]
    DomainCheck=url.split("/")
    if ProtocolCheck=="https":
        data.append("It has https protocol")
    elif ProtocolCheck=="http":
        data.append("It has http protocol")
    else:
        data.append("It has no http or https protocol")
        return data
    if len(DomainCheck)<3:
        data.append("It doesn't have domain")
        return data
    else:
        if DomainCheck[2]!="":
            data.append("Domain is:"+DomainCheck[2])
        else:
            data.append("It doesn't have domain")
            return data
        if len(DomainCheck)>3:
            for i in range(3,len(DomainCheck)):
                if "?" in DomainCheck[i]:
                    strPath=DomainCheck[i].split("?")
                    steps+=strPath[0]+","
                    params=strPath[1].split("&")
                    for i in params:
                        parameters+=i.replace("=",":")+","
                    data.append(parameters)
                else:
                    steps+=DomainCheck[i]+","
            data.append(steps)

    return data


