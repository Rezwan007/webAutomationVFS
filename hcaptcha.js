function getQueryVariable(variable, query) {
    var vars = query.split('&');
    for (var i = 0; i < vars.length; i++) {
        var pair = vars[i].split('=');
        if (decodeURIComponent(pair[0]) == variable) {
            return decodeURIComponent(pair[1]);
        }
    }
}


function get_site_key() {
    let iframes = document.getElementsByTagName("iframe");
    let iframe_src = iframes[0].getAttribute("src");
    let url = new URL(iframe_src);
    let url_fragments = url.hash.slice(1);
    let data_site_key = getQueryVariable('sitekey', url_fragments);
    return data_site_key;
}


function insert_token(token) {
    let iframes = document.getElementsByTagName("iframe");
    iframes[0].setAttribute("data-hcaptcha-response", token);
    let salt = iframes[0].getAttribute("data-hcaptcha-widget-id");
    document.getElementById("h-captcha-response-" + salt).innerHTML = token;
}


function submit_captcha(token) {

    window[widgetInfo.callback](token);
}