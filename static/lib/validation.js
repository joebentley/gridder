// Generated by CoffeeScript 1.8.0
(function() {
  $(function() {
    var validator;
    return validator = new FormValidator('grid', [
      {
        name: 'ylines',
        rules: 'required|numeric|greater_than[5]|less_than[50]'
      }, {
        name: 'file',
        rules: 'required'
      }
    ], function(errors, event) {
      var error, _i, _len;
      $("#errors").empty();
      for (_i = 0, _len = errors.length; _i < _len; _i++) {
        error = errors[_i];
        $("#errors").append('<li>' + error.message + '</li>');
      }
      return true;
    });
  });

}).call(this);
