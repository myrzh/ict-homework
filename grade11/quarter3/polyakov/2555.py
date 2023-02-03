print(
    len(
        list(
            filter(
                lambda x: x.count("S") == x.count("X"),
                open("24-s1.txt", encoding="utf-8").readlines(),
            )
        )
    )
)
