function atualizarAtributos() {
  var reduzir = document.getElementById("reduzirAtributos").checked;
  var com = document.getElementById("comButton");
  var manu = document.getElementById("manuButton");
  var cie = document.getElementById("cieButton");
  var sec = document.getElementById("secButton");
  
  if (reduzir) {
    com.innerHTML = "Comando: D" + (max_com - 2);
    manu.innerHTML = "Manutenção: D" + (max_manu - 2);
    cie.innerHTML = "Ciência: D" + (max_cie - 2);
    sec.innerHTML = "Segurança: D" + (max_sec - 2);
  } else {
    com.innerHTML = "Comando: D" + max_com;
    manu.innerHTML = "Manutenção: D" + max_manu;
    cie.innerHTML = "Ciência: D" + max_cie;
    sec.innerHTML = "Segurança: D" + max_sec;
  }
}

function gerarNumeroAleatorio(max) {
  var numero = Math.floor(Math.random() * max) + 1;
  document.getElementById("resultado").innerHTML = numero;
}

function aumentarEstresse() {
  var estresseAtual = parseInt(document.getElementById("estresse").innerHTML);
  if (estresseAtual < estresseMax) {
    estresseAtual += 1;
    document.getElementById("estresse").innerHTML = estresseAtual;
  }
}

function resetarEstresse() {
  document.getElementById("estresse").innerHTML = "0";
}
