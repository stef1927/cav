
var app = angular.module('mothers', ['smart-table']);

app.controller('MothersListCtrl', [
  '$scope', '$http', '$filter', function($scope, $http, $filter) {
    $scope.predicates = ['full_name'];
    $scope.selectedPredicate = $scope.predicates[0];
    $scope.itemsByPage = 10;
    $scope.numPages = 10;

    $scope.rowItems = [];
    return $http.get('/mothers/apis').then(function(result) {
      return angular.forEach(result.data, function(item) {
        return $scope.rowItems.push(item);
      });
    });
  }
]);

app.controller('ChildrenListCtrl', [
  '$scope', '$http', '$filter', function($scope, $http, $filter) {
    $scope.predicates = ['mother'];
    $scope.selectedPredicate = $scope.predicates[0];
    $scope.itemsByPage = 10;
    $scope.numPages = 10;

    $scope.rowItems = [];
    return $http.get('/children/apis').then(function(result) {
      return angular.forEach(result.data, function(item) {
        return $scope.rowItems.push(item);
      });
    });
  }
]);

app.controller('DonationsListCtrl', [
  '$scope', '$http', '$filter', function($scope, $http, $filter) {
    $scope.predicates = ['mother'];
    $scope.selectedPredicate = $scope.predicates[0];
    $scope.itemsByPage = 10;
    $scope.numPages = 10;

    $scope.rowItems = [];
    return $http.get('/donations/apis').then(function(result) {
      return angular.forEach(result.data, function(item) {
        return $scope.rowItems.push(item);
      });
    });
  }
]);

app.controller('OperatorsListCtrl', [
  '$scope', '$http', function($scope, $http) {

    $scope.rowItems = [];
    return $http.get('/operators/apis').then(function(result) {
      return angular.forEach(result.data, function(item) {
        return $scope.rowItems.push(item);
      });
    });
  }
]);


app.controller('MotherDetailsCtrl', [
  '$scope', '$http', function($scope, $http) {

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

    $scope.mother = [];
    return $http.get('/mother/id/apis').then(function(result) {
      return angular.forEach(result.data, function(item) {
        return $scope.mother.push(item);
      });
    });
}]);