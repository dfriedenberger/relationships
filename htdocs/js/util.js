

//read json and wait for response
read_json = function(url) {
    data = undefined
    $.ajax({
            dataType: "json",
            url: url,
            async: false, // wait for response
            success: function(data) {
                model = data
            }
    });
    return model
}


// First, checks if it isn't implemented yet.
if (!String.prototype.format) {
    String.prototype.format = function() {
        var args = arguments;
        return this.replace(/{(\d+)}/g, function(match, number) { 
        return typeof args[number] != 'undefined'
            ? args[number]
            : match
        ;
        });
    };
}


// Defining class in a Traditional Way.
function TributeManager(){
    this.tributes = {}
    this.attributes = {
        autocompleteMode: true,
        noMatchTemplate: "",
        values: [],
        selectTemplate: function(item) {
            if (typeof item === "undefined") return null;
            if (this.range.isContentEditable(this.current.element)) {
                return (
                '<span contenteditable="false"><a class="btn btn-primary btn-sm" style="margin: 2px" data-value="' +
                    item.original.value +
                    '" disabled="disabled">' +
                    item.original.key +
                    "</a></span>"
                );
            }
            return item.original.value;
        },
        menuItemTemplate: function(item) {
            return item.string;
        }
    };
};
 
TributeManager.prototype.getTribute = function(type){
    if (!Object.hasOwn(this.tributes,type))
    {
        this.tributes[type] = new Tribute(this.attributes);
    }
    return this.tributes[type] 
}


create_id = function(type,name) {
    return type+"/"+name.replace(/[^a-zA-Z0-9]/g,".").toLowerCase();
}