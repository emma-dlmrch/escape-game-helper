export function inlineHTML(text){
    let regex = /(<([^>]+)>)/ig;
    return text.replace(regex, "");
}