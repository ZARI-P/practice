favorite_language = {
    "sina": "javascript",
    "zahra": "typescript",
    "aylar": "python",
    "ali": "c",
    "sam": "c++"
}

for name, lang in favorite_language.items():
    print (f"{name} favorite programming language is {lang}")
    print("----------------------------------------------")
    
    for name in favorite_language.keys():
        print(name)
        print("-------------------------------------------")
        for lang in favorite_language.values():
            print(lang)