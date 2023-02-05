async function getDataFromPython() {
    var dates = await eel.get_date_details('2022-11-20')();
    console.log(dates)
    document.getElementById('header').innerText = dates;
}

document.getElementById('button').addEventListener('click', () => {
    getDataFromPython();
})