const family = {
    ron: "Ron",
    anne: "Jen",
    mae: "Mae",
    joy: "Joy",
    michael: "Michael",
    annie: "Annie"
}

const isFamily = name => {
    for (key in family) {
        if (name.toLowerCase().includes(key)) {
            return true;
        }
    }
    return false;
}