/* --- changes color of positive numbers to green, negative to red --- */
$('.percentChange').each(function(){
    var cellValue = $(this).html();
    if(!isNaN(parseFloat(cellValue))) {
      if (cellValue <= 0) {
        $(this).css('background-color','red');
      } 
      
      if(cellValue >= 0.001){
       $(this).css('color','green');
       }
    }
  });
