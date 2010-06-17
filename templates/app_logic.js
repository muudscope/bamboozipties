// Shared logic for the app

function delete_entry(id) {
  if( confirm("Delete Post?") ) {
    // They said yes

    var url = '/blog/delete/'+id+'.json';
    $.ajax({
      type: "POST",
      url: url,
      error: debug_error,
      success: function(data) {
        $("#post-id"+id).remove();
      }
    });

  }
  return false; // cancel's browser navigation
}

