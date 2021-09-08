data={
    "name": "John",
    "title": "Python Developer",
    "skills": [{
        "name": "coding",
        "level": "expert"
        },
        {
        "name": "documentation",
        "level": "basic"
    }]
}
for i in data["skills"]:
    print(i["name"])