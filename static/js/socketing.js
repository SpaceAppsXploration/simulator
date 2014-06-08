/**!
*
* Socketing
* Controls Communications Via Socket
*
* Copyright(c) 2014 Lorenzo <tunedconsulting@gmail.com>
* MIT Licensed
*
*/


'use strict'

var Socketing = {
    
    send_ack: function(msg, callback){
      var data;
        if (typeof callback == "function") {
      var callback = callback;
        }
        else var callback = null;
      if (sock && sock.readyState === 1) {
          
          sock.send(msg); //send message to server

          sock.onmessage = function(e) { //server messages receiver
              data = jQuery.parseJSON(e.data);
              
              //Handling different server responses
              if (data.data_type == 'get_target') {
                //show targets infos
                callback(data.data)

              }
              else if (data.data_type == 'get_physics'){
                //show physical infos
                callback(data.data)   

              }
              else if (data.data_type == 'destination-mission'){
                // checking if destination-mission combo is right
                if (data.data.code == 1) {
                    //error in combo
                    Designing.printError(data.data.message+" : "+ data.data.content)         
                }
                else callback() // >>> Go to stage 3
              }
              
              else { 
                /* just echo */ 
                Socketing.return_echo(data)
              }
            
          }
        }

    else console.log('Cannot send message. Socket is Closed!')
    },

    onopen: function() {
        console.log(msg)
        //console.log(sock.readyState)
        //clearInterval(recInterval);
        Socketing.send_ack('{"query": "get_target", "object": "' + $('#init').attr("data-id") + '"}', 
                            DOMFlow.getTarget)
    },

    onclose: function () {
        console.log('socket closed')
        //recInterval = setInterval(function () {
        //    connect(host, msg);
        //}, 2000);
    },

    raise_error: function(error){
      raise_error(error)
    },
    return_target: function(target){
      return_target(target)
    },
    return_physics: function(physics){
      return_physics(physics)
    },
    return_echo:  function(echo){
        return_echo(echo)
    }


};