def remove_vietnamese_characters(string):
  
  # every characters to lower case
  string = string.lower()

  # replace Vietnamese vowels with their base characters
  for vowel in ["à", "á", "ạ", "ả", "ã", "â", "ầ", "ấ", "ậ", "ẩ", "ẫ", "ă", "ằ", "ắ", "ặ", "ẳ", "ẵ"]:
    string = string.replace(vowel, "a")
  for vowel in ["è", "é", "ẹ", "ẻ", "ẽ", "ê", "ề", "ế", "ệ", "ể", "ễ"]:
    string = string.replace(vowel, "e")
  for vowel in ["ì", "í", "ị", "ỉ", "ĩ"]:
    string = string.replace(vowel, "i")
  for vowel in ["ò", "ó", "ọ", "ỏ", "õ", "ô", "ồ", "ố", "ộ", "ổ", "ỗ", "ơ", "ờ", "ớ", "ợ", "ở", "ỡ"]:
    string = string.replace(vowel, "o")
  for vowel in ["ù", "ú", "ụ", "ủ", "ũ", "ư", "ừ", "ứ", "ự", "ử", "ữ"]:
    string = string.replace(vowel, "u")
  for vowel in ["ỳ", "ý", "ỵ", "ỷ", "ỹ"]:
    string = string.replace(vowel, "y")
  
  # replace the special Vietnamese consonant with its base character
  string = string.replace("đ", "d")
  
  # remove diacritic marks
  string = string.replace(u"\u0300", "")
  string = string.replace(u"\u0301", "")
  string = string.replace(u"\u0303", "")
  string = string.replace(u"\u0309", "")
  string = string.replace(u"\u0323", "")
  string = string.replace(u"\u02C6", "")
  string = string.replace(u"\u0306", "")
  string = string.replace(u"\u031B", "")
  
  # return the result
  return string