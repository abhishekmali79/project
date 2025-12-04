
tax_rate = 0.08
def safe_int(value):
    try:
        return int(value)
    except:
        return 0
    
def dict_parser(text):
    if not text:
        return{},""

    items=text.split(",")
    d={}
    formatted_items=[]

    for item in items:
        if item.strip():
            if not item:
                continue

            try:
                key,value=item.split(":")
                value = value.split("=")[0]

                x,y=value.split("*")
                result=int(x)*int(y)

                key=key.strip()

                d[key]=int(result)
                formatted_items.append(f"{key}:{x}*{y}={d[key]}")

            except:
                continue
    
    formatted_text=",".join(formatted_items)
    return d,formatted_text


def calculate(NAME,DEBT,RAW_TEXT,PAID):

    debt = safe_int(DEBT)
    paid = safe_int(PAID)
    name=NAME
    raw_text=RAW_TEXT
    Dict,text=dict_parser(raw_text)
    Tdebt=sum(Dict.values())
    tax=round(Tdebt*tax_rate)
    total= safe_int(Tdebt + debt + tax)
    text=(f"{text}+{tax}")
    Tdebt=Tdebt+tax
    remaining=total-paid    

    return {
    "name": name,
    "debt": debt,
    "raw_text": raw_text,
    "text": text,
    "Tdebt": Tdebt,
    "total": total,
    "paid": paid,
    "remaining": remaining
    }