
$ ->
  validator = new FormValidator 'grid', [
    {
      name: 'ylines',
      rules: 'required|numeric|greater_than[5]|less_than[50]'
    },
    {
      name: 'file',
      rules: 'required'
    }],

    (errors, event) ->
      # Clear current errors
      do $("#errors").empty

      $("#errors").append '<li>' + error.message + '</li>' for error in errors
      return true

