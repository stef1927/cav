
var app = angular.module('mothers', []);

app.controller('ListCtrl', [
  '$scope', '$http', function($scope, $http) {
    $scope.items = [];
    return $http.get('apis').then(function(result) {
      return angular.forEach(result.data, function(item) {
        return $scope.items.push(item);
      });
    });
  }
]);


app.controller('MotherDetailsCtrl', [
  '$scope', '$http', function($scope, $http) {
    $scope.mother = [];
    return $http.get('/mother/id/apis').then(function(result) {
      return angular.forEach(result.data, function(item) {
        return $scope.posts.push(item);
      });
    });
  }
]);

app.controller('MotherDetailsCtrl', function($scope, $http) {
    $scope.modify_mother = function() {
        var in_data = { subject: $scope.subject };
        $http.post('mother/details', in_data)
            .success(function(out_data) {
                // do something
            });
    }
    $scope.reset_mother = function() {
        var in_data = { subject: $scope.subject };
        $http.post('mother/details', in_data)
            .success(function(out_data) {
                // do something
            });
    }
    $scope.print_mother = function() {
        var in_data = { subject: $scope.subject };
        $http.post('mother/details', in_data)
            .success(function(out_data) {
                // do something
            });
    }
    $scope.add_child = function() {
        var in_data = { subject: $scope.subject };
        $http.post('mother/details', in_data)
            .success(function(out_data) {
                // do something
            });
    }
    $scope.modify_child = function() {
        var in_data = { subject: $scope.subject };
        $http.post('mother/details', in_data)
            .success(function(out_data) {
                // do something
            });
    }
    $scope.delete_child = function() {
        var in_data = { subject: $scope.subject };
        $http.post('mother/details', in_data)
            .success(function(out_data) {
                // do something
            });
    }
    $scope.add_donation = function() {
        var in_data = { subject: $scope.subject };
        $http.post('mother/details', in_data)
            .success(function(out_data) {
                // do something
            });
    }
    $scope.modify_donation = function() {
        var in_data = { subject: $scope.subject };
        $http.post('mother/details', in_data)
            .success(function(out_data) {
                // do something
            });
    }
    $scope.delete_donation = function() {
        var in_data = { subject: $scope.subject };
        $http.post('mother/details', in_data)
            .success(function(out_data) {
                // do something
            });
    }
});