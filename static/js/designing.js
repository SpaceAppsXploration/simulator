/**!
*
* Designing
* Store Data And User Choices
*
* Copyright(c) 2014 Lorenzo <tunedconsulting@gmail.com>
* MIT Licensed
*
*/

'use strict'

var Designing = function(scope){
  var scope = scope
  var destination = null;
  var mission = null;
  var payload = {};
  var bus = {};
  var parameters = '';
  var simError = null;
};

Designing.prototype.setDestination = function(target){
      this.destination = target
      return false
    };

Designing.prototype.getDestination = function(){
      return this.destination
    };


Designing.prototype.getDestination = function(){
      return this.destination
    };

Designing.prototype.setMission = function(mission){
      this.mission = mission
      return false
    };

Designing.prototype.getMission = function(){
      return this.mission
    };

Designing.prototype.addPayload = function(name){
      this.payload['name'] = 'true'
      return false
    };

Designing.prototype.removePayload = function(name){
      delete this.payload['name'] 
    };

Designing.prototype.getPayload= function(){
      return this.payload
    };

Designing.prototype.addBus = function(name){
      this.bus['name'] = 'bustrue' 
      return false
    };

Designing.prototype.removeBus = function(name){
      delete this.bus['name']
      return false
    };

Designing.prototype.getBus = function(){
      return this.bus
    };

Designing.prototype.checkLoaded = function() {
      return {"destination": this.destination, "mission": this.mission,
              "bus": this.bus, "payload": this.payload}
    };

Designing.prototype.printParams = function() {
      this.parameters += '?destination=' + this.destination + '&mission=' + this.mission
      /*bus_keys = Object.keys(this.bus)
      payload_keys = Object.keys(this.payload)
      for (var i = 0; i < bus_keys.length; i++){
        this.parameters += '&' + bus_keys[i] + '=bus'
      }
      for (var i = 0; i < payload_keys.length; i++){
        this.parameters += '&' + payload_keys[i] + '=bustrue'
      }*/
      this.parameters
    };

Designing.prototype.getError = function(){
      this.simError
    };

Designing.prototype.setError = function(error){
      this.SimError = error;

    };

Designing.prototype.printError = function(error){
      this.simError = error
      alert(this.simError);
    };

