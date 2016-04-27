from __future__ import unicode_literals

from django.db import models

# Create your models here.

class MasterStatus(models.Model):
    id = models.BigIntegerField(primary_key=True)
    type = models.CharField(unique=True, max_length=10)
    last_updated_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'master_status'
    def __unicode__(self):
    	return u'%d: %s' % (self.id, self.type)

class MasterRepaymentType(models.Model):
    id = models.BigIntegerField(primary_key=True)
    repayment_type_name = models.CharField(max_length=255, blank=True, null=True)
    fk_status = models.ForeignKey(MasterStatus)
    last_modified_date = models.DateTimeField()
    last_modified_by = models.BigIntegerField()
    # fk_sci_client = models.ForeignKey('SciMasterClient')
    master_repayment_type_json = models.TextField(blank=True, null=True)  # This field type is a guess.

    def __unicode__(self):
       return u'%s' % (self.repayment_type_name)
    class Meta:
        managed = False
        db_table = 'master_repayment_type'

class MasterAuthor(models.Model):
    # testid = models.BigIntegerField()
    author = models.CharField(unique=True, max_length=10)
    text = models.CharField(unique=True, max_length=10)

    class Meta:
        managed = False
        db_table = 'master_author'
    def __unicode__(self):
        return u'%d: %s' % (self.author)