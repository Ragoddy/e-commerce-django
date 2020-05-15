// js for main fron markets
// js for products
function operateProductFormatter(value, row, index) {
    return [
      '<a class="enable btn btn-primary btn-circle" href="javascript:void(0)" title="Deshabilitar producto">',
      '<i class="fa fa-minus-square"></i>',
      '</a>  ',
      '<a class="remove btn btn-danger btn-circle" href="javascript:void(0)" title="Eliminar producto">',
      '<i class="fa fa-trash-alt"></i>',
      '</a>'
    ].join('')
}

window.operateProductEvents = {
    'click .enable': function (e, value, row, index) {
        alert('You click like action, row: ' + JSON.stringify(row))
    },
    'click .remove': function (e, value, row, index) {
        
    }
}

function imageProductFormatter(value, row) {
    console.log(row);
    return '<img class="text-center" src="' + row.image + '" alt="'+ row.title +'" height="40" width="60">'
}



$(document).ready(function() {
    
   
});
  