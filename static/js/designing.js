(function(exports, undefined) {
'use strict'

var Designing = function(){
  
  var destination = null;
  var mission = null;
  var payload = {};
  var bus = new Object();
  var parameters = '';
  var simError = null;

  return {
    setDestination: function(target){
      this.destination = target
      return false
    },
    getDestination: function(){
      return this.destination
    },
    setMission: function(mission){
      this.mission = mission
      return false
    },
    getMission: function(){
      return this.mission
    },
    addPayload: function(name){
      this.payload['name'] = 'true'
      return false
    },
    removePayload: function(name){
      delete this.payload['name'] 
    },
    getPayload: function(){
      return this.payload
    },
    addBus: function(name){
      this.bus['name'] = 'bustrue' 
      return false
    },
    removeBus: function(name){
      delete this.bus['name']
      return false
    },
    getBus: function(){
      return this.bus
    },
    checkLoaded: function() {
      return {"destination": this.destination, "mission": this.mission,
              "bus": this.bus, "payload": this.payload}
    },
    printParams: function() {
      this.parameters += '?destination=' + this.destination + '&mission=' + this.mission
      /*bus_keys = Object.keys(this.bus)
      payload_keys = Object.keys(this.payload)
      for (var i = 0; i < bus_keys.length; i++){
        this.parameters += '&' + bus_keys[i] + '=bus'
      }
      for (var i = 0; i < payload_keys.length; i++){
        this.parameters += '&' + payload_keys[i] + '=bustrue'
      }*/
      return this.parameters
    },
    getError: function(){
      return this.simError
    },
    setError: function(error){
      this.SimError = error;
      return false
    },
    printError: function(error){
      return alert(error);
    },
  }
}

});