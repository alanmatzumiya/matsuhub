var Diagram = MindFusion.Diagramming.Diagram;
var Behavior = MindFusion.Diagramming.Behavior;
var AbstractionLayer = MindFusion.AbstractionLayer;

var Font = MindFusion.Drawing.Font;
var Rect = MindFusion.Drawing.Rect;
var Text = MindFusion.Drawing.Text;
var Thickness = MindFusion.Drawing.Thickness;

var OrgChartNode = function (parent)
{
	AbstractionLayer.initializeBase(OrgChartNode, this, [parent]);

	this.setTitle('title');
	this.setFullName('full name');
	this.setNodeImageLocation('icon4.png');

	this.setShape('Rectangle');
	this.setText('node text');
	this.setBrush('#fff');
}

OrgChartNode.prototype =
{
	// draw logic
	updateCanvasElements: function (node)
	{
		AbstractionLayer.callBaseMethod(OrgChartNode, this, 'updateCanvasElements');

		// add the node image;
		if (this.nodeImage)
		{
			this.nodeImage.setBounds(new Rect(this.bounds.x, this.bounds.y + (this.bounds.height - 20) / 2, 20, 20));
			this.graphicsContainer.content.push(this.nodeImage);
		}

		// add the title label
		var titleFont = Font.copy(this.getEffectiveFont());
		var titleLabel = new Text(this.getTitle(),
			new Rect(this.bounds.x + 21, this.bounds.y + 5, this.bounds.width - 22, titleFont.size));
		titleLabel.font = titleFont;
		titleLabel.font.bold = true;
		titleLabel.fitInBounds = false;
		this.graphicsContainer.content.push(titleLabel);

		// add the name label
		var nameFont = Font.copy(this.getEffectiveFont());
		var nameLabel = new Text(this.getFullName(),
			new Rect(this.bounds.x + 21, this.bounds.y + 5 + titleFont.size, this.bounds.width - 22, nameFont.size));
		nameLabel.font = nameFont;
		nameLabel.pen = "blue";
		nameLabel.fitInBounds = false;
		this.graphicsContainer.content.push(nameLabel);

		// adjust the text label properties
		var textFont = Font.copy(this.getEffectiveFont());
		textFont.size = 3;
		var textRect = new Rect(this.bounds.x + 21, this.bounds.y + 3 + titleFont.size + nameFont.size, this.bounds.width - 22, this.bounds.height - 2 - titleFont.size - nameFont.size);
		this.text.font = textFont;
		this.text.textAlignment = Alignment.Near;
		this.text.lineAlignment = Alignment.Near;
		this.text.margin = new Thickness(1, 1, 1, 1);
		this.text.setBounds(textRect, 0);
	},

	loadNodeImage: function ()
	{
		this.nodeImage.loaded = true;
		if (this.parent)
			this.invalidate();
	},

	// properties
	getTitle: function ()
	{
		return this.title;
	},

	setTitle: function (value)
	{
		if (this.title !== value)
		{
			this.title = value;
		}
	},

	getFullName: function ()
	{
		return this.fullName;
	},

	setFullName: function (value)
	{
		if (this.fullName !== value)
		{
			this.fullName = value;
		}
	},

	getNodeImageLocation: function ()
	{
		return this.nodeImageLocation;
	},

	setNodeImageLocation: function (value)
	{
		if (this.nodeImageLocation != value)
		{
			this.nodeImageLocation = value;
			if (value)
			{
				this.nodeImage = new MindFusion.Drawing.Image(new Rect(this.bounds.x, this.bounds.y + (this.bounds.height - 20) / 2, 20, 20));
				AbstractionLayer.addHandlers(this.nodeImage.image, { load: AbstractionLayer.createDelegate(this, this.loadNodeImage) });
				this.nodeImage.image.src = value;
			}
		}
	}
};


var diagram = null;

$(document).ready(function ()
{
	AbstractionLayer.registerClass(OrgChartNode, "OrgChartNode", MindFusion.Diagramming.ShapeNode);

	// create a Diagram component that wraps the "diagram" canvas
	diagram = AbstractionLayer.createControl(Diagram, null, null, null, $("#diagram")[0]);

	// enable drawing of custom nodes interactively
	diagram.setCustomNodeType(OrgChartNode);
	diagram.setBehavior(Behavior.Custom);

	var node1 = new OrgChartNode(diagram);
	node1.setBounds(new Rect(25, 15, 60, 25));
	node1.setTitle("CEO");
	node1.setFullName("John Smith");
	node1.setText(
		"Our beloved leader. \r\n" +
		"The CEO of this great corporation.");
	node1.setNodeImageLocation("ceo.png");
	diagram.addItem(node1);

	var node2 = new OrgChartNode(diagram);
	node2.setBounds(new Rect(25, 55, 60, 25));
	node2.setTitle("CTO");
	node2.setFullName("Bob Smith");
	node2.setText("The technology chief of this great corporation.");
	node2.setNodeImageLocation("cto.png");
	diagram.addItem(node2);

	var node3 = new OrgChartNode(diagram);
	node3.setBounds(new Rect(95, 55, 60, 25));
	node3.setTitle("HR");
	node3.setFullName("Mary Johnson");
	node3.setText("Human resources and staff development.");
	node3.setNodeImageLocation("hr.png");
	diagram.addItem(node3);

	var node4 = new OrgChartNode(diagram);
	node4.setBounds(new Rect(175, 55, 60, 25));
	node4.setTitle("PR");
	node4.setFullName("Diana Brandson");
	node4.setText("Public relations and media.");
	node4.setNodeImageLocation("pr.png");
	diagram.addItem(node4);

	var node5 = new OrgChartNode(diagram);
	node5.setBounds(new Rect(175, 95, 60, 25));
	node5.setTitle("Media");
	node5.setFullName("Dave Lu");
	node5.setText("Adertising and creative content.");
	node5.setNodeImageLocation("ad.png");
	diagram.addItem(node5);

	diagram.getFactory().createDiagramLink(node1, node2);
	diagram.getFactory().createDiagramLink(node1, node3);
	diagram.getFactory().createDiagramLink(node1, node4);
	diagram.getFactory().createDiagramLink(node4, node5);
});