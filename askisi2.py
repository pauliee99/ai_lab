words=['fsafsdf', 'grfdDgrd', 'GVFDSGRDS', 'fds']

new_list = [i for i in range(len(words)) for i in range(len(words[i])) if words[i].islower() and len(words[i])>5] 
print (new_list)