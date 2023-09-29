val removeVietnameseCharacters = (string:String) => {

    // every characters to lower case
    var result = string.toLowerCase()

    // replace Vietnamese vowels with their base characters
    for (vowel <- List("à", "á", "ạ", "ả", "ã", "â", "ầ", "ấ", "ậ", "ẩ", "ẫ", "ă", "ằ", "ắ", "ặ", "ẳ", "ẵ")) {
        result = result.replace(vowel, "a")
    }
    for (vowel <- List("è", "é", "ẹ", "ẻ", "ẽ", "ê", "ề", "ế", "ệ", "ể", "ễ")) {
        result = result.replace(vowel, "e")
    }
    for (vowel <- List("ì", "í", "ị", "ỉ", "ĩ")) {
        result = result.replace(vowel, "i")
    }
    for (vowel <- List("ò", "ó", "ọ", "ỏ", "õ", "ô", "ồ", "ố", "ộ", "ổ", "ỗ", "ơ", "ờ", "ớ", "ợ", "ở", "ỡ")) {
        result = result.replace(vowel, "o")
    }
    for (vowel <- List("ù", "ú", "ụ", "ủ", "ũ", "ư", "ừ", "ứ", "ự", "ử", "ữ")) {
        result = result.replace(vowel, "u")
    }
    for (vowel <- List("ù", "ú", "ụ", "ủ", "ũ", "ư", "ừ", "ứ", "ự", "ử", "ữ")) {
        result = result.replace(vowel, "u")
    }
    for (vowel <- List("ỳ", "ý", "ỵ", "ỷ", "ỹ")) {
        result = result.replace(vowel, "y")
    }

    // replace the special Vietnamese consonant with its base character
    result = result.replace("đ", "d")

    // remove diacritic marks
    for (mark <- List("\u0300", "\u0301", "\u0303", "\u0309", "\u0323", "\u02C6", "\u0306", "\u031B")) {
        result = result.replace(mark, "")
    }

    // return the result
    result
}