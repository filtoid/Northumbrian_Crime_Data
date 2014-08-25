
var crimeDataApp = angular.module('crimeDataApp', []);

crimeDataApp.controller('CrimeListCtrl', function ($scope, $http) {

   $http({method: 'GET', url: 'http://data.police.uk/api/' +
   'crimes-at-location?date=2012-02&lat=52.629729&lng=-1.131592'}).
    success(function(data, status, headers, config) {
      $scope.crimes = data
      // this callback will be called asynchronously
      // when the response is available

    }).
    error(function(data, status, headers, config) {
      // called asynchronously if an error occurs
      // or server returns response with an error status.
    });

});