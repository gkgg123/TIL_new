html_string = input()[6:-7].split('</div>')


for row in html_string:
    if row.strip():
        start_index = row.find('title="')
        if start_index == -1:
            continue
        end_index = row.index('"',start_index+7)
        title = row[start_index+7:end_index].strip()
        print(f'title : {title}')

        cur_idx = 0
        while True:
            p_tag_start = row.find('<p>',cur_idx)
            if p_tag_start == -1:
                break
            p_tag_close = row.find('</p>',p_tag_start)
            temp = []
            bracket_open = False
            for t in row[p_tag_start+3:p_tag_close]:
                if t == '<':
                    bracket_open = True
                    continue
                if t == '>':
                    bracket_open = False
                    continue
                if not bracket_open:
                    temp.append(t)
            complete_string = ''.join(temp).strip()

            while complete_string.find('  ') != -1:
                complete_string = complete_string.replace('  ',' ')
            print(complete_string)
            cur_idx = p_tag_close
                
        