const change = () => {
    const testy = /[0-9A-Fa-f]{6}/g;
    const check_hex = "#"
    let bg_hex = document.getElementById('hex-code').value;
    
    if(bg_hex.startsWith(check_hex)) {
        if(testy.test(bg_hex)) {
            document.querySelector('body').style.background = bg_hex;
        } else {
            alert("Please make sure to enter a valid hex code!")
        }
    } else {
        alert("Please make sure you put in the hashtag!")
    }
}