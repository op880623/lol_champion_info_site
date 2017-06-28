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

    $scope.has_selected_column = function () {
        about_hp = $scope.show_hp || $scope.show_hpperlevel || $scope.show_hpmax || $scope.show_hpregen || $scope.show_hpregenperlevel || $scope.show_hpregenmax;
        about_mp = $scope.show_mp || $scope.show_mpperlevel || $scope.show_mpmax || $scope.show_mpregen || $scope.show_mpregenperlevel || $scope.show_mpregenmax;
        about_attack = $scope.show_attackdamage || $scope.show_attackdamageperlevel || $scope.show_attackdamagemax || $scope.show_attackspeed || $scope.show_attackspeedperlevel || $scope.show_attackspeedmax;
        about_armor = $scope.show_armor || $scope.show_armorperlevel || $scope.show_armormax || $scope.show_spellblock || $scope.show_spellblockperlevel || $scope.show_spellblockmax;
        about_other = $scope.show_movespeed || $scope.show_attackrange;
        return about_hp || about_mp || about_attack || about_armor || about_other;
    }
    $scope.show_column = function (item) {
        return item || !$scope.has_selected_column();
    }

// pagination
    $scope.page = 1;
    $scope.items_per_page = 25;
    $scope.page_sub = function () {
        $scope.page = $scope.page - 1;
    }
    $scope.page_add = function () {
        $scope.page = $scope.page + 1;
    }
    $scope.is_first_page = function () {
        return $scope.page === 1;
    }
    $scope.is_last_page = function () {
        return $scope.page * $scope.items_per_page >= $scope.champions.length;
    }
    $scope.page_start = function () {
        return ($scope.page - 1) * $scope.items_per_page;
    }
    $scope.item_index = function (index) {
        return $scope.page_start() + index + 1;
    }

// order
    $scope.order = 'eng_name';
    // change column which list is ordered by
    $scope.order_by = function (order) {
        if ($scope.order.replace(/-/i, '') === order && $scope.order.search(/-/i) >= 0) {
            $scope.order = order;
        }
        else {
            $scope.order = '-' + order;
        }
    }
    // colorize column which list is ordered by
    $scope.is_ordered = function (order) {
        var entry = $scope.order.replace(/-/i, '');
        return order === entry;
    }

// colorize row which mouse on
    $scope.selectedRow = null;
    $scope.set_selected = function (selectedRow) {
        $scope.selectedRow = selectedRow;
    };
    $scope.is_selected = function (index) {
        return index === $scope.selectedRow;
    }


    $scope.format_time = function (time) {
        return time.replace(/ /i, 'T');
    }
});
