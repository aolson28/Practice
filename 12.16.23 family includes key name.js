const family = {
    ron: "dad",
    anne: "mom",
    mae: "child1",
    joy: "child2",
    michael: "child3",
    annie: "child4"
}

const isFamily = name => {
    for (key in family) {
        if (name.toLowerCase().includes(key)) {
            return true;
        }
    }
    return false;
}
