<template>
    <v-container fluid>
        <v-layout>
            <v-flex xs10>
                <v-data-table
                    :headers="header"
                    :items="localidades"
                >
                    <template
                        v-slot:items="props"
                    >
                        <td>{{ props.index + 1 }}</td>
                        <td>
                            <a
                                :href="getLocalidadeUrl(props.item.id)">
                                {{ props.item.nome }}
                            </a>
                        </td>
                        <td>{{ props.item.bioma }}</td>
                        <td>{{ props.item.clima }}</td>
                    </template>
                </v-data-table>
            </v-flex>
        </v-layout>
    </v-container>
</template>
<script>
import { mapActions, mapGetters } from 'vuex';

export default {
    name: 'ListarLocalidades',
    data() {
        return {
            header: [
                {
                    text: '#',
                    align: 'left',
                    sortable: false,
                    value: 'numero',
                },
                {
                    text: 'nome',
                    value: 'nome',
                },
                {
                    text: 'bioma',
                    value: 'bioma',
                },
                {
                    text: 'clima',
                    value: 'clima',
                },
            ],
            localidades: [],
        };
    },
    watch: {
         listaLocalidades() {
             this.localidades = this.listaLocalidades;
         },
    },
    created() {
        this.buscarLocalidades();
    },
    methods: {
        ...mapActions({
            buscarLocalidades: 'localidade/buscarLocalidades',
        }),
        getLocalidadeUrl(id) {
            return `localidade/` + id;
        },
    },
    computed: {
        ...mapGetters({
            listaLocalidades: 'localidade/localidades',
        }),
    },
};
</script>
