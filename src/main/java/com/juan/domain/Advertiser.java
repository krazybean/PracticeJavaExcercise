package com.juan.domain;

public class Advertiser extends ObjectWithId{
    private String Name;
    private String Contact;
    private int CreditLimit;

    public Advertiser(){

    }

    public Advertiser(long id, String Name, String Contact, int CreditLimit){
        super(id);
        this.Name = Name;
        this.Contact = Contact;
        this.CreditLimit = CreditLimit;
    }

    public String getName(){
        return Name;
    }

    public String getContact(){
        return Contact;
    }

    public int getCreditLimit(){
        return CreditLimit;
    }

    @Override
    public boolean equals(Object o){
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;

        Advertiser advertiser = (Advertiser) o;

        return id == advertiser.id;
    }

    public void setName(String Name){
        this.Name = Name;
    }

    public void setContact(String Contact){
        this.Contact = Contact;
    }

    public void setCreditLimit(int creditLimit) {
        CreditLimit = creditLimit;
    }

    @Override
    public int hashCode(){
        return (int) (id ^ (id >>> 32));
    }
}