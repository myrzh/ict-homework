print(*sorted(list(set([(int(f'11{i}223'), int(f'11{i}223') // 149)
      for i in [f'{a}{b}{c}' for a in list(range(0, 10)) + ['']
      for b in list(range(0, 10)) + [''] for c in list(range(0, 10)) + ['']]
      if int(f'11{i}223') % 149 == 0])), key=lambda x: x[0]), sep='\n')
