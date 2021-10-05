function check() 
    {

      let a = "{{selectbtn}}";

      if (a == "Passive") {
        document.getElementById("btn1").focus();
      }
      if (a == "Freedrive") {
        document.getElementById("btn2").focus();
      }
      if (a == "Active isotonic") {
        document.getElementById("btn3").focus();
      }
      if (a == "Active isometric") {
        document.getElementById("btn4").focus();
      }
      if (a == "cctive isokinetic") {
        document.getElementById("btn5").focus();
      }
      let z = "{{uname}}";

    window.onload = check;

    function passive() {

      document.getElementById("btnselect").value = "Passive";
    }

    function passive1() {

      document.getElementById("btnselect").value = "Freedrive";
    }

    function passive2() {

      document.getElementById("btnselect").value = "Active isotonic";
    }

    function passive3() {

      document.getElementById("btnselect").value = "Active isometric";
    }
    function passive4() {

      document.getElementById("btnselect").value = "Acctive isokinetic";
    }
  }

  function myprofile(clr) {
    location.href = clr;
}

function openNav() {
    document.getElementById("mySidenav").style.width = "350px";
  }

  function closeNav() {
   document.getElementById("mySidenav").style.width = "0";
  }
