document.getElementById('personal').addEventListener('click', function () {
    document.getElementById('textPersonal').style.display = 'none';
    document.getElementById('textLaboral').style.display = 'block';
    document.getElementById('textAcademica').style.display = 'none';
    document.getElementById('textHabilidades').style.display = 'none';
})

document.getElementById('laboral').addEventListener('click', function () {
    document.getElementById('textPersonal').style.display = 'none';
    document.getElementById('textLaboral').style.display = 'none';
    document.getElementById('textAcademica').style.display = 'block';
    document.getElementById('textHabilidades').style.display = 'none';
})

document.getElementById('academica').addEventListener('click', function () {
    document.getElementById('textPersonal').style.display = 'none';
    document.getElementById('textLaboral').style.display = 'none';
    document.getElementById('textAcademica').style.display = 'none';
    document.getElementById('textHabilidades').style.display = 'block';
})

document.getElementById('habilidades').addEventListener('click', function () {
    document.getElementById('textPersonal').style.display = 'block';
    document.getElementById('textLaboral').style.display = 'none';
    document.getElementById('textAcademica').style.display = 'none';
    document.getElementById('textHabilidades').style.display = 'none';
})