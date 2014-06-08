/**!
*
* DOMFlow
* Controls Presentation In The Browser 
*
* Copyright(c) 2014 Lorenzo <tunedconsulting@gmail.com>
* MIT Licensed
*
*/


'use strict'

var DOMFlow = {
  startDesign: function(element){
    var destination = element.attr("destination")
    $('#stage-1').fadeOut('slow');
    $('#stage-2').fadeIn('slow');
    $('body').addClass('milkyway');
    Designing.setDestination(destination)
    console.log(Designing.getDestination())
    $('#show-dest2').text('Your mission is going to ' + destination)
  },
  goToBusDesign: function(){
    $('#stage-2').fadeOut('slow');
    $('#stage-3').fadeIn('slow');
    DOMFlow.scrollUp()
    Designing.setError(null)
    
    var target = Designing.getDestination()
    var mission = Designing.getMission()
    $('#show-dest3').text('Your mission is going to ' + target)
    $('#show-dest3').parent().parent().append('<li><i class="glyphicon glyphicon-ok"></i><span>Mission goal: '+ mission +'</span></li>')
  },
  getTarget: function(json){
    $('#controls').attr('body', json.id)
    $('#controls-data').text("");

    $('#controls-data').append('<img class="media-object img-rounded img-responsive targets" src="'+json.image_url+'"/>');
    $('#controls-data').append('<p>'+json.characteristics+'</p>');
  },
  getPhysics: function(json){
    if(json.code == 1){ $('#controls-data').text("no data for this body"); return false}
    
    $('#controls-data').text("");
    delete json.target
    delete json.discover
    delete json.name
    var physics = JsonHuman.format(json);
    //console.log(physics)
    $('#controls-data').append('<div id="t-resp" class="table-responsive"></div>');
    $('#t-resp').append(physics);
  },
  scrollUp: function(){
    $('html, body').animate({scrollTop:0}, 'slow');
    /*$('.popupPeriod').fadeIn(1000, function(){
        setTimeout(function(){$('.popupPeriod').fadeOut(2000);}, 3000);
    });*/
  },
};