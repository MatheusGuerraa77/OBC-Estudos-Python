def file_read_from_line(fname, nlines):
    from itertools import islice
    with open (fname, encoding="utf8") as file:
        for line in islice(file, nlines):
            print(line)
            
file_read_from_line("dados/texto.txt", 2)