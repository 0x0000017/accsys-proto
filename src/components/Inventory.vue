<template>
  <div>
    <br>
    <v-card elevation = '2' outlined>
      <v-card-title>Sales Record</v-card-title>
      <v-data-table
        :headers="headers"
        :items="sales"
        :items-per-page="5"
        class="elevation-1">
      </v-data-table>
    </v-card> 
  <br><br>

  <v-card elevation = '2' outlined>
  <v-card-title>Add Item</v-card-title>
  <form>
    <v-text-field
      v-model="product_name"
      :error-messages="nameErrors"
      :counter="100"
      label="Product Name"
      required
      @input="$v.product_name.$touch()"
      @blur="$v.product_name.$touch()"
    ></v-text-field>
    <v-text-field
      v-model="quantity_ordered"
      :error-messages="qErrors"
      :counter="100"
      label="Quantity Ordered"
      required
      @input="$v.quantity_ordered.$touch()"
      @blur="$v.quantity_ordered.$touch()"
    ></v-text-field>
    <v-text-field
      v-model="price_each"
      :error-messages="pErrors"
      :counter="100"
      label="Price Each"
      required
      @input="$v.price_each.$touch()"
      @blur="$v.price_each.$touch()"
    ></v-text-field>
    <v-text-field
      v-model="order_date"
      :error-messages="oErrors"
      :counter="100"
      label="Order Date"
      required
      @input="$v.order_date.$touch()"
      @blur="$v.order_date.$touch()"
    ></v-text-field>
    <v-text-field
      v-model="purchase_addr"
      :error-messages="paErrors"
      :counter="100"
      label="Purchase Address"
      required
      @input="$v.purchase_addr.$touch()"
      @blur="$v.purchase_addr.$touch()"
    ></v-text-field>

    <v-btn
      class="mr-4"
      @click="submit"
    >
      submit
    </v-btn>
    <v-btn @click="clear">
      clear
    </v-btn>
    <br>
  </form>
  </v-card>

  </div>
</template>


<script>

  import { validationMixin } from 'vuelidate'
  import { required, maxLength, email } from 'vuelidate/lib/validators'

  import axios from 'axios';
  export default {
    mixins: [validationMixin],
    validations: {
      product_name: { required, maxLength: maxLength(100) },
      email: { required },
      select: { required },
    },
    data() {
      return {
        sales: [],
        headers: [
          {
            text: 'Order ID',
            align: 'start',
            sortable: 'false',
            value: 'order_id'
          },
          { text: 'Product Name', value: 'product_name'},
          { text: 'Quantity Ordered', value: 'quantity_ordered'},
          { text: 'Price Each', value: 'price_each'},
          { text: 'Order Date', value: 'order_date'},
          { text: 'Purchase Address', value: 'purchase_addr'}
        ],
        product_name: '',
        quantity_ordered: '',
        price_each: '',
        order_date: '',
        purchase_addr: ''
      }; 
    },
    computed: {
      nameErrors () {
        const errors = []
        if (!this.$v.product_name.$dirty) return errors
        !this.$v.product_name.maxLength && errors.push('Name must be at most 100 characters long')
        !this.$v.product_name.required && errors.push('Name is required.')
        return errors
      },
      qErrors () {
        const errors = []
        if (!this.$v.quantity_ordered) return errors
        !this.$v.quantity_ordered.maxLength && errors.push('Name must be at most 100 characters long')
        !this.$v.quantity_ordered.required && errors.push('Name is required.')
        return errors
      },
      pErrors () {
        const errors = []
        if (!this.$v.price_each) return errors
        !this.$v.price_each.maxLength && errors.push('Name must be at most 100 characters long')
        !this.$v.price_each.required && errors.push('Name is required.')
        return errors
      },
      oErrors () {
        const errors = []
        if (!this.$v.order_date) return errors
        !this.$v.order_date.maxLength && errors.push('Name must be at most 100 characters long')
        !this.$v.order_date.required && errors.push('Name is required.')
        return errors
      },
      paErrors () {
        const errors = []
        if (!this.$v.purchase_addr) return errors
        !this.$v.purchase_addr.maxLength && errors.push('Name must be at most 100 characters long')
        !this.$v.purchase_addr.required && errors.push('Name is required.')
        return errors
      },
    },
    methods: {
      async getSales() {
        const path = 'http://localhost:5000/sales';
        axios.get(path)
          .then((res) => {
            console.log(res);
            this.sales = res.data;
          })
          .catch((error) => {
            console.error(error);
          });
      },
      submit () {
        this.$v.$touch()
      },
      clear () {
        this.$v.$reset()
        this.product_name = ''
        this.quantity_ordered = ''
        this.price_each = ''
        this.order_date = ''
        this.purchase_addr = ''
      },
    },
    created() {
      this.getSales();
    },
  };
</script>