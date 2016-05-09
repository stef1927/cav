
var app = angular.module('mothers', ['ngResource', 'smart-table',  'ui.bootstrap']);

app.config(['$locationProvider', function($locationProvider) {
  $locationProvider.html5Mode(true);
}]);

app.factory('Children', [ '$resource', function($resource) {
    return $resource('/children/apis');
}]);

app.factory('Child', [ '$resource', function($resource) {
  return $resource('/children/:id/apis', { id: '@id' },  { 'update': { method:'PUT' } });
}]);

app.factory('Donations', [ '$resource', function($resource) {
    return $resource('/donations/apis');
}]);

app.factory('Donation', [ '$resource', function($resource) {
  return $resource('/donations/:id/apis', { id: '@id' },  { 'update': { method:'PUT' } });
}]);

app.factory('Mothers', [ '$resource', function($resource) {
    return $resource('/mothers/apis');
}]);

app.factory('Mother', [ '$resource', function($resource) {
  return $resource('/mothers/:id/apis', { id: '@id' },  { 'update': { method:'PUT' } });
}]);

app.factory('Operators', [ '$resource', function($resource) {
    return $resource('/operators/apis');
}]);

app.controller('MothersListCtrl', function($scope, $http, $filter) {
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
);

app.controller('ChildrenListCtrl', function($scope, $http, $filter) {
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
);

app.controller('DonationsListCtrl', function($scope, $http, $filter) {
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
);

app.controller('OperatorsListCtrl', function($scope, $http) {

    $scope.rowItems = [];
    return $http.get('/operators/apis').then(function(result) {
      return angular.forEach(result.data, function(item) {
        return $scope.rowItems.push(item);
      });
    });
  }
);

app.controller('MotherDetailsCtrl',  function($scope, $location, $resource, $uibModal, $log,
                                              Mother, Child, Donation,
                                              Mothers, Children, Donations, Operators) {

    $scope.mother = Mother.get({id: $location.path().split("/")[2]});
    $scope.operators = Operators.query();
    $scope.backend_date_format = 'DD/MM/YYYY';
    $scope.today = new Date();

    $scope.save_mother = function() {
        $scope.mother.$save();
    };

    $scope.reset_mother = function() {

    };

    $scope.print_mother = function() {
        alert("Non ancora disponibile");
    };

    // Children

    $scope.add_child = function() {
        var modalInstance = $uibModal.open({
            animation: true,
            templateUrl: 'child-details.html',
            controller: 'ChildDetailsCtrl',
            size: 'lg',
            resolve: {
                child: function () {
                    var child = {mother: $scope.mother.id, date_of_birth: $scope.today};
                    $log.info("Creating " + JSON.stringify(child));
                    return child;
                },
            title: function () {
                return 'Nuovo bimbo';
            },
            backend_date_format: function () {
                return $scope.backend_date_format;
            }
        }});

        modalInstance.result.then(function (child) {
            var mother = $scope.mother;
            $log.info("Saving " + JSON.stringify(child));

            Children.save([], child, function(c) {
               $log.info("Child saved: " + JSON.stringify(c));
               $scope.mother.children.push(c);
            }, function(err) {
                alert(JSON.stringify(err));
            });
        });
    };


    $scope.edit_child = function(id) {
        Child.get({id: id}, function(child) {
            child.date_of_birth = new Date(moment(child.date_of_birth, $scope.backend_date_format).toISOString());
            $log.info('Retrieved for modification: ' + JSON.stringify(child));
            var modalInstance = $uibModal.open({
                animation: true,
                templateUrl: 'child-details.html',
                controller: 'ChildDetailsCtrl',
                size: 'lg',
                resolve: {
                    child: function () {
                        $log.info("Modifying " + JSON.stringify(child));
                        return child;
                    },
                    title: function () {
                        return 'Modifica bimb' + (child.sex == 'F' ? 'a' : 'o');
                    },
                    backend_date_format: function () {
                        return $scope.backend_date_format;
                    }
            }});

            modalInstance.result.then(function (child) {
                $log.info("Saving " + JSON.stringify(child));

                child.$update(function(c) {
                   $log.info("Child modified: " + JSON.stringify(c));
                   $scope.mother.children.forEach(function(cc, i) { if (cc.id == c.id) $scope.mother.children[i] = c; });
                }, function(err) {
                    alert(JSON.stringify(err));
                });
            });
        });
    };

    $scope.delete_child = function(id) {
        var child = Child.get({id: id}, function(child) {
            $log.info("Deleting " + JSON.stringify(child));

            var modalInstance = $uibModal.open({
                animation: true,
                templateUrl: 'question.html',
                controller: 'QuestionCtrl',
                size: 'lg',
                resolve: {
                    title: function () {
                        return 'Cancella bimb' + (child.sex == 'F' ? 'a' : 'o');
                },
                message: function () {
                    return 'Si desidera cancellare ' + child.name + '?';
                },
            }});

            modalInstance.result.then(function () {
               child.$delete(function(c) {
                   $log.info("Child deleted: " + JSON.stringify(c));
                   $scope.mother.children = $scope.mother.children.filter(function(c) { return c.id != id });
               }, function(err) {
                  alert(JSON.stringify(err));
               });
            });
        });
    };

    // Donations
    $scope.donation = {};

    $scope.save_donation = function() {
        //TODO -validation and add donation to mother
        $scope.mother.save();
    };

    $scope.reset_donation = function() {
        $scope.donation = {};
        $scope.mother.save();
    };
});

app.controller('QuestionCtrl', function ($scope, $log, $uibModalInstance, title, message) {
    $scope.title = title;
    $scope.message = message;
    $scope.ok = function () {
        $uibModalInstance.close('ok');
    };

    $scope.cancel = function () {
        $uibModalInstance.dismiss('cancel');
    };
});

app.controller('ChildDetailsCtrl', function ($scope, $log, $uibModalInstance, child, title, backend_date_format) {
    $scope.child = child;
    $scope.title = title;
    $scope.genders = ['F', 'M', '-'];

    $scope.ok = function () {
        var child = $scope.child;
        child.date_of_birth = moment(child.date_of_birth).format(backend_date_format);
        $uibModalInstance.close(child);
    };

    $scope.cancel = function () {
        $uibModalInstance.dismiss('cancel');
    };

    $scope.opened = false;
    $scope.clear = function () {
        $scope.child.date_of_birth = null;
    };

    $scope.open = function($event) {
        $log.info("Opening");
        $event.preventDefault();
        $event.stopPropagation();
        $scope.opened = true;
        $log.info("Opened");
    };

    $scope.dateOptions = {
        formatYear: 'yyyy',
        startingDay: 1
    };

    $scope.formats = ['dd/MM/yyyy'];
    $scope.format = $scope.formats[0];
});