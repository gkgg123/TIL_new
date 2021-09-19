html_string = input()[6:-7].split('</div>')


for row in html_string:
    if row:
        p_split = row.split('<p>')
        for ind,val in enumerate(p_split):
            if ind:
                bracket_open = False
                temp = []
                for st in val:
                    if st == '<':
                        bracket_open = True
                    elif st == '>':
                        bracket_open = False
                    elif not bracket_open:
                        temp.append(st)
                complete_str = ''.join(temp).strip()
                while complete_str.find('  ') != -1:
                    complete_str = complete_str.replace('  ',' ')
                print(complete_str)
            else:
                start_index = val.find('title="') + 7
                end_index = val.find('"',start_index)
                title = val[start_index:end_index].strip()
                print(f'title : {title}')
                
