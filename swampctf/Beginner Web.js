const CryptoJS = require("crypto-js");

let part1 = "w3b_"
let key = "flagPart2_3";
let encryptedPart2 = "U2FsdGVkX1/oCOrv2BF34XQbx7f34cYJ8aA71tr8cl8=";
let encryptedPart3 = "U2FsdGVkX197aFEtB5VUIBcswkWs4GiFPal6425rsTU=";

let part2 = CryptoJS.AES.decrypt(encryptedPart2, key).toString(CryptoJS.enc.Utf8);
let part3 = CryptoJS.AES.decrypt(encryptedPart3, key).toString(CryptoJS.enc.Utf8);
console.log("Part 1:", part1);
console.log("Part 2:", part2);
console.log("Part 3:", part3);
console.log(`Flag is: swampCTF{${part1}${part2}${part3}}`);

// Part 1: w3b_
// Part 2: br0w53r5_4r3_
// Part 3: c0mpl1c473d
// Flag is: swampCTF{w3b_br0w53r5_4r3_c0mpl1c473d}