def counting_words(file_content):
       wordsCount = len(file_content.split())
       return(wordsCount)


def character_counter(file_content):
    savePoint = {}
    
    for char in file_content.lower():
        if char in savePoint:
            savePoint[char] += 1
        else:
            savePoint[char] = 1
    
    return(savePoint)
     
def report(file_content):
    print('--- Begin Report of books/frankenstein.txt ---')
    print(f"{counting_words(file_content)} words found in the document")
    
    registry = character_counter(file_content)
    for key, value in registry.items():
        print(f"The '{key}' was found {value} times")
    
    
    print('--- BEnd Report ---')
        
       

               
    
def main():
    with open("books/frankenstein.txt") as f:
        file_content = f.read()
        print(file_content)
        counting_words(file_content)
        character_counter(file_content)
        report(file_content)
    

main()