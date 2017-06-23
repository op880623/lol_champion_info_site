var name_all = 'Champion Information Table';
var name_update = 'Reccent Update Champion';
var url_all = "/";
var url_update = "/reccent_update/";


var app = angular.module('myApp', []);
app.controller('customersCtrl', function($scope, $http) {
    if (window.location.pathname.search(/reccent_update/i) >= 0) {
        $http.get("/reccent_update_champion/").then(function (response) {
            $scope.champions = response.data.data;
        });
        $scope.update_page = true;
        document.getElementById('title').prepend(name_update+'/');
        document.getElementById('link').innerHTML = name_all;
        document.getElementById('link').href = url_all;
    }
    else {
        $http.get("/all_data/").then(function (response) {
            $scope.champions = response.data.data;
        });
        $scope.update_page = false;
        document.getElementById('title').prepend(name_all+'/');
        document.getElementById('link').innerHTML = name_update;
        document.getElementById('link').href = url_update;
    }


    $scope.order = 'eng_name';
    $scope.order_by = function (order) {
        if ($scope.order.replace(/-/i, '') === order && $scope.order.search(/-/i) >= 0) {
            $scope.order = order;
        }
        else {
            $scope.order = '-' + order;
        }
    }
    $scope.is_ordered = function (order) {
        var entry = $scope.order.replace(/-/i, '');
        return order === entry;
    }


    $scope.selectedRow = null;
    $scope.set_selected = function (selectedRow) {
        $scope.selectedRow = selectedRow;
    };
    $scope.is_selected = function (index) {
        return index === $scope.selectedRow;
    }


    $scope.format_time = function (time) {
        return time.replace(/\.\d+\+00:00/i, '')
    }
});
