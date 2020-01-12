from django.shortcuts import render

# Create your views here.


def form(request):
    cxt = {}
    cxt['number'], cxt['data1'] = '0', ''
    cxt['data2'], cxt['sym'], cxt['error'] = '', '', ''
    request.encoding = 'utf-8'
    if request.POST:
        data1, data2 = request.POST['data1'], request.POST['data2']
        sym = request.POST['sym']
        if 'digit' in request.POST:
            num = request.POST['digit']
            if not data1:
                res1, res2, display = num, data2, num
            elif not sym:
                res1, res2, display = data1+num, data2, data1+num
            else:
                if ord(sym) == 247 and num == '0' and (not data2):
                    cxt['error'] = ' 0 can not be divided ! '
                    sym, display, res1, res2 = '', '0', '', ''
                elif ord(sym) == 61:
                    sym, display, res1, res2 = '', num, num, ''
                else:
                    res1, res2, display = data1, data2+num, data2+num
            cxt['sym'], cxt['number'], cxt['data1'], cxt['data2'] = sym, display, res1, res2
        elif 'symbol' in request.POST:
            symbol = request.POST['symbol']
            if not data1:
                cxt['error'] = 'The first value shouold be a digit, not an operator ! '
                sym, display, res1, res2 = '', '0', '', ''
            elif sym and (not data2):
                if ord(sym) == 61:
                    sym, display, res1, res2 = symbol, data1, data1, ''
                else:
                    cxt['error'] = '2 continuous operators is invalid ! '
                    sym, display, res1, res2 = '', '0', '', ''
            elif not sym:
                res1, display, res2 = data1, data1, data2
                if ord(symbol) == 61:
                    sym = ''
                else:
                    sym = symbol
            else:
                if ord(sym) == 43:
                    res1 = str(int(int(data1) + int(data2)))
                elif ord(sym) == 8722:
                    res1 = str(int(int(data1) - int(data2)))
                elif ord(sym) == 215:
                    res1 = str(int(int(data1) * int(data2)))
                elif ord(sym) == 247:
                    res1 = str(int(int(data1) / int(data2)))
                display, res2 = res1, ''
                sym = symbol
            cxt['sym'], cxt['number'], cxt['data1'], cxt['data2'] = sym, display, res1, res2
    return render(request, "Calculator.html", cxt)
