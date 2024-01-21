//how many encryptions are there??????
//there is a saying that only the username must match to be login
//base 64 = R0kzREdSUlRHUVpUSU0yRUdJM0RHUlJVR0UyRFNOQlhHTVpESU5JPQ==
// Userhash:    R0kzREdaUlRHUVpUSU0zRUdJM0RHWlJVR0UyRFNOQlhHTVpESU5JPQ==



let username = "R0kzREdaUlRHUVpUSU0zRUdJM0RHWlJVR0UyRFNOQlhHTVpESU5JPQ=="

function msg1(){
    alert("yooo mate chill y u tryin to change password of the account that u dont even own ^_^ bruhhhh")
}

function msg2(){
    alert("This system doesnt even have a Database!!! How are u goin to create a account")
    console.log("This system doesnt even have a Database!!! How are u goin to create a account")

}
function encryption1() {
    // Assuming "username" is the ID of an input element, you need to use quotes around it.
    var usernameEnt = document.getElementById("username").value
    // Check if the username is not empty before proceeding with encryption transformation.
    if (usernameEnt) {
        // Different variable name for encryption transformation
        var encryptedUsername = ""
        for (var i = 0; i < usernameEnt.length; i++) {
            var charCode = usernameEnt.charCodeAt(i)
            if (charCode >= 65 && charCode <= 90) {
                encryptedUsername += String.fromCharCode(((charCode - 65 + 13) % 26) + 65);
            } else if (charCode >= 97 && charCode <= 122) {
                encryptedUsername += String.fromCharCode(((charCode - 97 + 13) % 26) + 97);
            } else {
                encryptedUsername += usernameEnt.charAt(i)
            }
        }
        console.log("Original username:", usernameEnt);
        console.log("Encrypted username:", encryptedUsername);
        // encryptedUsername
        encryption2(encryptedUsername)
    } else {
        console.log("Username is empty");
    }
    return null
}
function customTransform(input) {
    var output = "";
    for (var i = 0; i < input.length; i++) {
        var charCode = input.charCodeAt(i);
        if (charCode >= 33 && charCode <= 126) {
            output += String.fromCharCode(((charCode - 33 + 47) % 94) + 33);
        } else {
            output += input.charAt(i);
        }
    }
    return output;
}
function encryption2(userhash) {
    if (userhash) {
        console.log("Userhash:", userhash);
        // Convert userhash to a custom transformation
        var userhashTransformed = customTransform(userhash)
        console.log("Userhash (Transformed):", userhashTransformed)
        encryption3(userhashTransformed)
    } else {
        console.log("Userhash is empty")
    }
}

function encryption3(userhash2) {
    if (userhash2) {
        console.log("Transformed userhash:", userhash2);
        var userhashBase16 = convertToBase16(userhash2)
        console.log("Userhas:", userhashBase16)
        encryption4(userhashBase16)
    } else {
        console.log("Userhash is empty");
    }
}

function convertToBase16(input) {
    var hexString = '';
    for (var i = 0; i < input.length; i++) {
        var hexCharCode = input.charCodeAt(i).toString(16);
        hexString += hexCharCode.length === 1 ? '0' + hexCharCode : hexCharCode;
    }
    return hexString;
}


function encryption4(userhash3) {
    if (userhash3) {
        console.log(" userhash:", userhash3);
        var userhashBase32 = convertToBase32(userhash3);
        console.log("Userhash:", userhashBase32);
        encryption5(userhashBase32)
    } else {
        console.log("Userhash is empty");
    }
}

function convertToBase32(input) {
    var base32Chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ234567';
    var bits = '';
    var base32String = '';

    for (var i = 0; i < input.length; i++) {
        var binary = input.charCodeAt(i).toString(2).padStart(8, '0');

        bits += binary;

        while (bits.length >= 5) {
            var chunk = bits.slice(0, 5);
            bits = bits.slice(5);
            base32String += base32Chars[parseInt(chunk, 2)];
        }
    }

    // Handle any remaining bits
    if (bits.length > 0) {
        // If there are remaining bits, add padding and convert to base32
        var padding = '0'.repeat(5 - bits.length);
        bits += padding;
        base32String += base32Chars[parseInt(bits, 2)];
    }

    // Add padding '=' characters to ensure proper length
    while (base32String.length % 8 !== 0) {
        base32String += '=';
    }

    return base32String;
}


function encryption5(userhash4) {
    if (userhash4) {
        console.log("Userhash4:", userhash4);
        var userhashBase64 = convertToBase64(userhash4);
        console.log("Userhash:", userhashBase64);
        //for login
        if (userhashBase64 == username){
            alert("nicu")
            window.location.href = 'falg.html'; // Redirect to dopes.html after successful login
        }
        else(
            alert("login failed")
        )
    } else {
        console.log("Userhash is empty");
    }
}

function convertToBase64(input) {
    // Use btoa function for base64 encoding in browsers
    return btoa(input);
}

