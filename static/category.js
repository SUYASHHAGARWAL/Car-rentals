$(document).ready(function () {
  $.getJSON("http://localhost:8000/api/json_displaycategory", function (data) {
    $("#categoryid").append($("<option>").text("-Select Category-"));
    data.map((item) => {
      $("#categoryid").append($("<option>").text(item.categoryname).val(item.id));
    });
  });

  $("#categoryid").change(function () {
    $.getJSON("http://localhost:8000/api/jsondisplaysubcategory",{'cddid':$('#categoryid').val()}, function (data) {
      $("#subcategoryid").empty()
      $("#subcategoryid").append($("<option>").text("-Select Brand-"))
      console.log(data)
      // var l=Object.keys(data)
      // var p=Object.values(data)    
      data.map((item) => {
      console.log('start')
        $("#subcategoryid").append($("<option>").text(item.subcategoryname).val(item.id));
      });
    });
  });
  $(function() {
    $( "#modelyear" ).datepicker();
});
});
